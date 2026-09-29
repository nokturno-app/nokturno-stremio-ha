# Čistý Python bez závislostí mimo standardní knihovnu; oficiální obraz je pro amd64, aarch64 i armv7.
FROM python:3.12-slim
# Kód doplňku není v tomhle repu: stáhne se při sestavení z veřejného vydání (ověřený SHA-256).
# Novější verze pak zavaděč stahuje sám do /data/verze.
ARG NOKTURNO_UPDATE_URL=https://raw.githubusercontent.com/nokturno-app/nokturno-stremio-app/main/update.json
COPY stahni.py zavadec.py /
RUN python3 /stahni.py "$NOKTURNO_UPDATE_URL" /app && rm /stahni.py
ENV PYTHONUNBUFFERED=1
CMD ["python3", "/zavadec.py"]
