import json
from liquid import Template
import markdown

DATA_DIR = "data"
TEMPLATE_DIR = "templates"

def read_template(file_path):
	with open(file_path, 'r', encoding='utf-8') as file:
		return file.read()

def render_template(template_str, data):
	# Transform text
	text_list = []
	for key in data["text"].keys():
		text_list += [[key, markdown.markdown(data["text"][key])]]
	data["text"] = text_list

	# Transform politedissent data
	if "politedissent" in data:
		text_list = []
		for text in data["politedissent"]["text"]:
			for key in text.keys():
				text_list += [[key, markdown.markdown(text[key])]]
		data["politedissent"]["text"] = text_list

	if "housemdguide" in data:
		data["converter"] = {"patient": "Patient", 'involvment': "Origin of the Case", 'ethics': "Ethics", 'steps': "Steps taken to Diagnose", 'diagnosis': "Diagnosis", 'diagnosis_origin': "Origin of the diagnosis", 'additional': "Additional Information"}

	template = Template(template_str)
	return template.render(data)

def convert_markdown_to_html(markdown_content):
	return markdown.markdown(markdown_content)

def load_data(filename):
	with open(filename, "r") as f:
		return json.load(f)

if __name__ == "__main__":
	data = load_data(f"{DATA_DIR}/data.json")

	template = read_template("episode.html")
	html = render_template(template, data["7"]["8"])

	with open("_site/test.html", "w") as f:
		f.write(html)