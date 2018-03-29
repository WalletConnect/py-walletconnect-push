import sys
import argparse
import asyncio
import aiohttp
import uvloop
from aiohttp import web

from wallet_connect_push.push_notifications import PushNotificationsService, FirebaseError

routes = web.RouteTableDef()

FCM_SERVER_KEY='fcm.server.key'
PUSH_SERVICE='io.wallet.connect.push_notifications'

def error_message(message):
  return {"message": message}


@routes.get('/hello')
async def hello(request):
  return web.Response(text="hello world, this is Wallet Connect Push")


@routes.post('/send-push-notification')
async def send_push_notification(request):
  try:
    request_json = await request.json()
    bridge_webhook = request_json['bridgeWebhook']
    fcm_token = request_json['fcmToken']
    transaction_uuid = request_json['transactionUuid']
    notification_details = request_json['notificationDetails']
    notification_title = notification_details['notificationTitle']
    notification_body = notification_details['notificationBody']

    # Send push notification
    push_notifications_service = request.app[PUSH_SERVICE]
    data_message = {"bridge_webhook": bridge_webhook, "transactionUuid": transaction_uuid}
    await push_notifications_service.notify_single_device(
        registration_id=fcm_token,
        message_title=notification_title,
        message_body=notification_body,
        data_message=data_message)
    return web.json_response(status=200)
  except KeyError:
    return web.json_response(error_message("Incorrect input parameters"), status=400)
  except TypeError:
    return web.json_response(error_message("Incorrect JSON content type"), status=400)
  except FirebaseError:
    return web.json_response(error_message("Error pushing notifications through Firebase"), status=500)
  except:
      return web.json_response(error_message("Error unknown"), status=500)


async def initialize_push_notifications(app):
  fcm_server_key = app[FCM_SERVER_KEY]
  if fcm_server_key:
    app[PUSH_SERVICE] = PushNotificationsService(debug=True)
  else:
    session = aiohttp.ClientSession(loop=app.loop)
    app[PUSH_SERVICE] = PushNotificationsService(session=session, api_key=fcm_server_key)


async def close_push_notification_connection(app):
  if app[PUSH_SERVICE].session:
    await app[PUSH_SERVICE].session.close()


def main(): 
  parser = argparse.ArgumentParser()
  parser.add_argument('--fcm-server-key', type=str, default=None, help='Server FCM key')
  parser.add_argument('--host', type=str, default='localhost')
  parser.add_argument('--port', type=int, default=8081)
  args = parser.parse_args()

  app = web.Application()
  app[FCM_SERVER_KEY] = args.fcm_server_key
  app.on_startup.append(initialize_push_notifications)
  app.on_cleanup.append(close_push_notification_connection)
  app.router.add_routes(routes)
  asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
  web.run_app(app, host=args.host, port=args.port)


if __name__ == '__main__':
  main()
