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
# notification_repository MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.notification_log import NotificationLog


class NotificationRepository:

    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_notification_log(self,
                            log: NotificationLog):
        
        self.db.add(log)
        await self.db.commit()
        await self.db.refresh(log)

        return log
    
    async def get_user_notifications(self, user_id: str):

        result = await self.db.execute(
            select(NotificationLog).where(
                NotificationLog.user_id == user_id
            )
        )

        return result.scalars().all()
    
    async def update_status(self, notification_id: str,
                            status: str):
        
        result = await self.db.execute(
            select(NotificationLog).where(
                NotificationLog.notification_id == notification_id
            )
        )

        log = result.scalar_one_or_none()

        if log:
            log.status = status
            await self.db.commit()
            await self.db.refresh(log)
        
        return log
