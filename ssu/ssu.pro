TEMPLATE = subdirs

config.files = ssu.ini
config.path  = /etc/ssu

static_config.files = repos.ini ssu-defaults.ini
static_config.path  = /usr/share/ssu

INSTALLS += config static_config
