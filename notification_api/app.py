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
# app MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
from fastapi import FastAPI
from notification_api.routes.notification_routes import router as notification_router
from notification_api.middleware.auth_middleware import AuthMiddleware
from utils.logger import get_logger
from config.settings import settings

logger = get_logger()


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.APP_NAME,
        version="1.0.0"
    )

    # Middleware
    app.add_middleware(AuthMiddleware)

    # Routes
    app.include_router(notification_router,
                       prefix="/notifications")
    
    @app.get("/health")
    async def health_check():
        return {"status": "ok"}
    
    logger.info("Notification API initialized")

    return app
