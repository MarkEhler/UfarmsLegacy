from flask import request

output, sunrise, sunset = loop_data_collect(int(request.form['time_span']), request.form['location'], request.form['date'])
day_dict = process(output, int(request.form['time_span']), sunrise, sunset)