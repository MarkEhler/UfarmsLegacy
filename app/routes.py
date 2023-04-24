from flask import render_template, flash, redirect, url_for, request, Response, session
from app import app
from app.forms import SimForm
from app.api_calls import *
import os, io, json
# draw figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas


@app.route('/')
@app.route('/dashboard', methods=['GET', 'POST'])
def form():
    form = SimForm()
    if request.method == 'GET':
        session.clear()
        print(len(session))
    print(len(session))
    if form.validate_on_submit():
        flash(f'Building graph for {form.time_span.data} days...')
        return redirect(url_for('results'))
    return render_template('form.html', title='Welcome', form=form)

@app.route('/about')
def about():
	return render_template('about.html', title='About')

@app.route('/results', methods=['GET', 'POST'])
def handle_data():
    output, sunrise, sunset = loop_data_collect(int(request.form['time_span']), request.form['location'], request.form['date'])
    listed, avgs = process(output, int(request.form['time_span']), sunrise, sunset)
    for idx, i in enumerate(listed):
        session[str(idx)] = i
    print(len(session))
    return render_template('results.html', title='Sunny Day(s)', avgs=avgs)


@app.route('/plot.png')
def plot_png():
    fig = create_figure(session)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')