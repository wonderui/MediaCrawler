from waitress import serve

import mc_api

serve(mc_api.app, host='0.0.0.0', port=7001, threads=50, channel_timeout=90)
