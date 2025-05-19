ready/report.pdf: report/report.pdf
	mkdir -p ./ready
	cp report/report.pdf ready/report.pdf

ready/stud-unit-test-report-prev.json: code/stud-unit-test-report-prev.json
	mkdir -p ./ready
	cp code/stud-unit-test-report-prev.json ready/stud-unit-test-report-prev.json

ready/app-cli-debug:
	mkdir -p ./ready
	cp -r code/* ready/

