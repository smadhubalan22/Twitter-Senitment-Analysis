from app import app, api
import app.scb_forms.views as form_views
from flask_cors import CORS  # Verification

CORS(app)  #


if __name__ == '__main__':
    api.add_namespace(form_views.form_ns)
    app.run(host='0.0.0.0', port=8005)




#
# from app import app, api
# import app.wersel_forms.views as form_views
# # import pytz, os
# # from datetime import datetime,  date, timedelta
# # from dateutil.relativedelta import relativedelta
# from flask_cors import CORS
# CORS(app)
#
# if __name__ == '__main__':
#
#     api.add_namespace(form_views.form_ns)
#     app.run(host='0.0.0.0', port=8005)
