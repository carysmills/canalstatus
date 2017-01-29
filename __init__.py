from flask import Flask, render_template
import csv
app = Flask(__name__)

@app.route('/')
def main():

	with open('/var/www/canalstatus/canalstatus/canaldata.csv', 'r') as csvfile:
		csvcontent = csv.reader(csvfile, delimiter='|')
		for row in csvcontent:
			continue

	# return '%s %s' % (row[0], row[1])

	info = row[0]

	return render_template('index.html', name=info)

if __name__ == '__main__':
	app.run(debug=True)