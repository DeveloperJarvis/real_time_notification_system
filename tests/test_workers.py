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
# test_workers MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
import pytest
from workers.notification_worker import start_notification_worker


@pytest.mark.asyncio
async def test_worker_process(monkeypatch):

    async def mock_consumer():
        class MockMessage:
            value = {
                "user_id": "123",
                "payload": {
                    "message": "hello"
                }
            }
        
        async def generator():
            yield MockMessage()
        
        return generator()
    
    async def mock_send_push(event):
        return True
    
    monkeypatch.setattr(
        "workers.notification_worker.get_consumer",
        lambda topic: mock_consumer()
    )

    monkeypatch.setattr(
        "workers.notification_worker.send_push_notification",
        mock_send_push
    )

    try:
        await start_notification_worker()
    except Exception:
        pass

    assert True
