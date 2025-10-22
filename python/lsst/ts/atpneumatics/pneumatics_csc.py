# This file is part of ts_atpneumatics.
#
# Developed for the Vera Rubin Observatory Telescope and Site Systems.
# This product includes software developed by the LSST Project
# (https://www.lsst.org).
# See the COPYRIGHT file at the top-level directory of this distribution
# for details of code ownership.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

__all__ = ["ATPneumaticsCsc", "run_atpneumatics"]

import asyncio
import pathlib

from lsst.ts import attcpip, salobj

from . import __version__
from .config_schema import CONFIG_SCHEMA
from .enums import Command
from .pneumatics_simulator import PneumaticsSimulator


class ATPneumaticsCsc(attcpip.AtTcpipCsc):
    """CSC for the auxiliary telescope pneumatics controller.

    Parameters
    ----------
    initial_state : `salobj.State` or `int` (optional)
        The initial state of the CSC. This is provided for unit testing,
        as real CSCs should start up in `State.STANDBY`, the default.

    Notes
    -----
    **Events**

    * cellVentsState
    * eStop
    * instrumentState
    * m1CoverLimitSwitches
    * m1CoverState
    * m1State
    * m1VentsLimitSwitches
    * m1VentsPosition
    * m2State
    * mainValveState
    * powerStatus
    """

    version = __version__

    def __init__(
        self,
        config_dir: str | pathlib.Path | None = None,
        check_if_duplicate: bool = False,
        initial_state: salobj.State = salobj.State.STANDBY,
        override: str = "",
        simulation_mode: int = 0,
    ) -> None:
        super().__init__(
            name="ATPneumatics",
            index=0,
            config_schema=CONFIG_SCHEMA,
            config_dir=config_dir,
            initial_state=initial_state,
            override=override,
            simulation_mode=simulation_mode,
        )

        # PenumaticsSimulator for simulation_mode == 1.
        self.simulator: PneumaticsSimulator | None = None

    async def start_clients(self) -> None:
        if self.simulation_mode == 1 and self.simulator is None:
            self.simulator = PneumaticsSimulator(
                host=self.config.host,
                cmd_evt_port=self.config.cmd_evt_port,
                telemetry_port=self.config.telemetry_port,
            )
            await self.simulator.configure()
        await super().start_clients()

    async def do_closeInstrumentAirValve(self, data: salobj.BaseMsgType) -> None:
        self.assert_enabled("closeInstrumentAirValve")
        await self.cmd_closeInstrumentAirValve.ack_in_progress(data, self.cmd_done_timeout)
        self.log.debug("Sending closeInstrumentAirValve.")
        async with asyncio.timeout(self.cmd_done_timeout):
            command_issued = await self.write_command(command=Command.CLOSE_INSTRUMENT_AIR_VALE)
            await command_issued.done

    async def do_closeM1CellVents(self, data: salobj.BaseMsgType) -> None:
        self.assert_enabled("closeM1CellVents")
        await self.cmd_closeM1CellVents.ack_in_progress(data, self.cmd_done_timeout)
        self.log.debug("Sending closeM1CellVents.")
        async with asyncio.timeout(self.cmd_done_timeout):
            command_issued = await self.write_command(command=Command.CLOSE_M1_CELL_VENTS)
            await command_issued.done

    async def do_closeM1Cover(self, data: salobj.BaseMsgType) -> None:
        self.assert_enabled("closeM1Cover")
        await self.cmd_closeM1Cover.ack_in_progress(data, self.cmd_done_timeout)
        self.log.debug("Sending closeM1Cover.")
        async with asyncio.timeout(self.cmd_done_timeout):
            command_issued = await self.write_command(command=Command.CLOSE_M1_COVER)
            await command_issued.done

    async def do_closeMasterAirSupply(self, data: salobj.BaseMsgType) -> None:
        self.assert_enabled("closeMasterAirSupply")
        await self.cmd_closeMasterAirSupply.ack_in_progress(data, self.cmd_done_timeout)
        self.log.debug("Sending closeMasterAirSupply.")
        async with asyncio.timeout(self.cmd_done_timeout):
            command_issued = await self.write_command(command=Command.CLOSE_MASTER_AIR_SUPPLY)
            await command_issued.done

    async def do_m1CloseAirValve(self, data: salobj.BaseMsgType) -> None:
        self.assert_enabled("m1CloseAirValve")
        await self.cmd_m1CloseAirValve.ack_in_progress(data, self.cmd_done_timeout)
        self.log.debug("Sending m1CloseAirValve.")
        async with asyncio.timeout(self.cmd_done_timeout):
            command_issued = await self.write_command(command=Command.M1_CLOSE_AIR_VALVE)
            await command_issued.done

    async def do_m1SetPressure(self, data: salobj.BaseMsgType) -> None:
        self.assert_enabled("m1SetPressure")
        await self.cmd_m1SetPressure.ack_in_progress(data, self.cmd_done_timeout)
        self.log.debug("Sending m1SetPressure.")
        async with asyncio.timeout(self.cmd_done_timeout):
            command_issued = await self.write_command(command=Command.M1_SET_PRESSURE, pressure=data.pressure)
            await command_issued.done

    async def do_m2CloseAirValve(self, data: salobj.BaseMsgType) -> None:
        self.assert_enabled("m2CloseAirValve")
        await self.cmd_m2CloseAirValve.ack_in_progress(data, self.cmd_done_timeout)
        self.log.debug("Sending m2CloseAirValve.")
        async with asyncio.timeout(self.cmd_done_timeout):
            command_issued = await self.write_command(command=Command.M2_CLOSE_AIR_VALVE)
            await command_issued.done

    async def do_m1OpenAirValve(self, data: salobj.BaseMsgType) -> None:
        self.assert_enabled("m1OpenAirValve")
        await self.cmd_m1OpenAirValve.ack_in_progress(data, self.cmd_done_timeout)
        self.log.debug("Sending m1OpenAirValve.")
        async with asyncio.timeout(self.cmd_done_timeout):
            command_issued = await self.write_command(command=Command.M1_OPEN_AIR_VALVE)
            await command_issued.done

    async def do_m2OpenAirValve(self, data: salobj.BaseMsgType) -> None:
        self.assert_enabled("m2OpenAirValve")
        await self.cmd_m2OpenAirValve.ack_in_progress(data, self.cmd_done_timeout)
        self.log.debug("Sending m2OpenAirValve.")
        async with asyncio.timeout(self.cmd_done_timeout):
            command_issued = await self.write_command(command=Command.M2_OPEN_AIR_VALVE)
            await command_issued.done

    async def do_m2SetPressure(self, data: salobj.BaseMsgType) -> None:
        self.assert_enabled("m2SetPressure")
        await self.cmd_m2SetPressure.ack_in_progress(data, self.cmd_done_timeout)
        self.log.debug("Sending m2SetPressure.")
        async with asyncio.timeout(self.cmd_done_timeout):
            command_issued = await self.write_command(command=Command.M2_SET_PRESSURE, pressure=data.pressure)
            await command_issued.done

    async def do_openInstrumentAirValve(self, data: salobj.BaseMsgType) -> None:
        self.assert_enabled("openInstrumentAirValve")
        await self.cmd_openInstrumentAirValve.ack_in_progress(data, self.cmd_done_timeout)
        self.log.debug("Sending openInstrumentAirValve.")
        async with asyncio.timeout(self.cmd_done_timeout):
            command_issued = await self.write_command(command=Command.OPEN_INSTRUMENT_AIR_VALVE)
            await command_issued.done

    async def do_openM1CellVents(self, data: salobj.BaseMsgType) -> None:
        self.assert_enabled("openM1CellVents")
        await self.cmd_openM1CellVents.ack_in_progress(data, self.cmd_done_timeout)
        self.log.debug("Sending openM1CellVents.")
        async with asyncio.timeout(self.cmd_done_timeout):
            command_issued = await self.write_command(command=Command.OPEN_M1_CELL_VENTS)
            await command_issued.done

    async def do_openM1Cover(self, data: salobj.BaseMsgType) -> None:
        self.assert_enabled("openM1Cover")
        await self.cmd_openM1Cover.ack_in_progress(data, self.cmd_done_timeout)
        self.log.debug("Sending openM1Cover.")
        async with asyncio.timeout(self.cmd_done_timeout):
            command_issued = await self.write_command(command=Command.OPEN_M1_COVER)
            await command_issued.done

    async def do_openMasterAirSupply(self, data: salobj.BaseMsgType) -> None:
        self.assert_enabled("openMasterAirSupply")
        await self.cmd_openMasterAirSupply.ack_in_progress(data, self.cmd_done_timeout)
        self.log.debug("Sending openMasterAirSupply.")
        async with asyncio.timeout(self.cmd_done_timeout):
            command_issued = await self.write_command(command=Command.OPEN_MASTER_AIR_SUPPLY)
            await command_issued.done


def run_atpneumatics() -> None:
    """Run the ATPneumatics CSC."""
    asyncio.run(ATPneumaticsCsc.amain(index=None))
