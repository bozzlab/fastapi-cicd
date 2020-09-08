#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Peem Srinikorn
# Created Date: Tue Sep  8 20:57:59 +07 2020
# =============================================================================

from app.handlers import app
import uvicorn

if __name__ == "__main__":
    uvicorn.run("main:app", host = '0.0.0.0', port = 8080, reload = True, debug = True)
