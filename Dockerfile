FROM python:3.7-alpine

ARG weasyprint_version=51

# Required packages from https://weasyprint.readthedocs.io/en/stable/install.html#alpine
RUN apk add --no-cache --update \
    gcc \
    musl-dev \
    jpeg-dev \
    zlib-dev \
    libffi-dev \
    cairo-dev \
    pango-dev \
    gdk-pixbuf-dev \
    msttcorefonts-installer \
    fontconfig \
    && update-ms-fonts && fc-cache -f

# Install pip dependencies
RUN pip install \
    flask \
    weasyprint==$weasyprint_version

# Copy the application
COPY /app /app

WORKDIR /app

# Define Flask run configuration
ENV FLASK_APP=server.py
ENV FLASK_ENV=production

EXPOSE 5000

# Run flask
CMD [ "flask", "run", "--host=0.0.0.0" ]
