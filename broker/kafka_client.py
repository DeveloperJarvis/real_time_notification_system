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
# kafta_client MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
import json
import asyncio
from aiokafka import AIOKafkaProducer, AIOKafkaConsumer
from config.settings import settings

producer = None


async def get_producer():
    global producer
    if producer is None:
        producer = AIOKafkaProducer(
            bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS,
            value_serializer=lambda v: json.dumps(v).encode("utf-8"),
            retry_backoff_ms=1000,
            request_timeout_ms=30000
        )

        # retry loop
        for i in range(3):
            try:
                await producer.start()
                break
            except Exception:
                print(f"Retrying Kafta connection... {i}")
                await asyncio.sleep(2)
    return producer


async def stop_producer():
    global producer
    if producer:
        await producer.stop()
        producer = None


async def get_consumer(topic: str):
    consumer = AIOKafkaConsumer(
        topic,
        bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS,
        value_deserializer=lambda v: json.loads(v.decode("utf-8")),
        group_id="notification-workers"
    )
    await consumer.start()
    return consumer


async def stop_consumer(consumer):
    if consumer:
        await consumer.stop()
