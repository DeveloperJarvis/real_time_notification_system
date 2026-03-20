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
# notification_worker MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
from broker.kafka_client import get_consumer
from broker.topics import PUSH_TOPIC
from delivery.push_delivery_service import send_push_notification
from utils.logger import get_logger

logger = get_logger()


async def start_notification_worker():
    consumer = await get_consumer(PUSH_TOPIC)
    logger.info("Push notification worker started")
    try:
        async for message in consumer:
            event = message.value
            try:
                await send_push_notification(event)
            except Exception as e:
                logger.error(f"Push notification failed: {e}")
    except Exception as e:
        logger.error(f"Worker crashed: {e}")
    finally:
        await consumer.stop()
