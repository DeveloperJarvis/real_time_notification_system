# --------------------------------------------------
# -*- Python -*- Compatibility Header
#
# Copyright (C) 2023 Developer Jarvis (Pen Name)
#
# This file is part of the Real-Time Notification System Library. This library is free
# software; you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the
# Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#
# Real-Time Notification System - Push notifications using pub/sub model
# Skills: messaging systems, async IO
#
# Author: Developer Jarvis (Pen Name)
# Contact: https://github.com/DeveloperJarvis
#
# --------------------------------------------------

# --------------------------------------------------
# main MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
import asyncio
import uvicorn

from notification_api.app import create_app
from workers.notification_worker import start_notification_worker
from workers.email_worker import start_email_worker
from workers.sms_worker import start_sms_worker

from websocket_gateway.gateway_server import app as websocket_app
from config.settings import settings
from utils.logger import get_logger
from broker.kafka_client import stop_producer

logger = get_logger()
api_app = create_app()


async def start_workers():
    """
    Start background Kafka workers
    """

    logger.info("Starting notification workers...")
    await asyncio.gather(
        start_notification_worker(),
        start_email_worker(),
        start_sms_worker(),
    )


async def start_api():
    """
    Start FastAPI HTTP server
    """
    
    config = uvicorn.Config(
        api_app,
        host=settings.API_HOST,
        port=int(settings.API_PORT),
        log_level=settings.LOG_LEVEL.lower(),
    )
    server = uvicorn.Server(config)
    await server.serve()


async def main():
    logger.info("Starting Real-Time Notification System")
    try:
        await start_api()
    finally:
        await stop_producer()


if __name__ == "__main__":
    asyncio.run(main())
