#!/usr/bin/env dockerfile
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Peem Srinikorn
# Created Date: Tue Sep  8 20:57:59 +07 2020
# =============================================================================

FROM python:3.6-slim
LABEL maintainer "Peem Srinikorn"
ADD . / 
RUN apt-get update \ 
    && apt-get install gcc -y \
    && pip install --no-cache-dir -r requirements.txt \
    && rm -rf /var/lib/apt/lists/* 
CMD ["python", "main.py"]
