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
# device_repository MODULE
# --------------------------------------------------

# --------------------------------------------------
# imports
# --------------------------------------------------
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.user_device import UserDevice


class DeviceRepository:

    def __init__(self, db: AsyncSession):
        self.db = db
    
    async def get_user_devices(self, user_id: str):

        result = await self.db.execute(
            select(UserDevice).where(UserDevice.user_id == user_id)
        )

        return result.scalars().all()
    
    async def add_device(self, device: UserDevice):

        self.db.add(device)
        await self.db.commit()
        await self.db.refresh(device)

        return device
    
    async def delete_device(self, user_id: str, device_id: str):

        result = await self.db.execute(
            select(UserDevice).where(
                UserDevice.user_id == user_id,
                UserDevice.device_id == device_id
            )
        )

        device = result.scalar_one_or_none()

        if device:
            await self.db.delete(device)
            await self.db.commit()

        return device
