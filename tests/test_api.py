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
# test_api MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
import pytest
from fastapi.testclient import TestClient
from notification_api.app import create_app
from config.settings import settings

app = create_app()
client = TestClient(app)


@pytest.fixture
def headers():
    return {
        "x-api-key": settings.API_KEY
    }


def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_send_notification(headers, monkeypatch):
    
    async def mock_publish(*args, **kwargs):
        return True
    
    monkeypatch.setattr(
        "notification_api.services.publish_service.publish_event",
        mock_publish
    )

    payload = {
        "user_id": "user123",
        "event_type": "NEW_MESSAGE",
        "channel": "push",
        "payload": {
            "message": "Hello!"
        }
    }

    response = client.post(
        "/notifications/send",
        json=payload,
        headers=headers
    )

    assert response.status_code == 200
    assert response.json()["message"] == "Notification queued successfully"


def test_auth_failure():

    payload = {
        "user_id": "123",
        "event_type": "TEST",
        "channel": "push",
        "payload": {}
    }

    response = client.post(
        "/notifications/send",
        json=payload
    )

    assert response.status_code == 401
