from flask import Flask, render_template
import csv
app = Flask(__name__)

@app.route('/')
def main():

	with open('/var/www/canalstatus/canalstatus/canaldata.csv', 'r') as csvfile:
		csvcontent = csv.reader(csvfile, delimiter='|')
		for row in csvcontent:
			continue

	ready = row[0].lower()
	infoformatted = row[1] 
	datetime = row[2]

	return render_template('index.html', ready=ready, infoformatted=infoformatted, datetime=datetime)

if __name__ == '__main__':
	app.run(debug=True)