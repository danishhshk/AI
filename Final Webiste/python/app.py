from flask import Flask, render_template, request, send_file
from fpdf import FPDF

app = Flask(__name__)

# Your partnership deed generation code goes here (as provided in your question)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_deed():
    # Retrieve form data
    partner_names = [request.form[f'partner_name{i}'] for i in range(1, 5)]
    # Retrieve other form data here

    # Generate the partnership deed using your existing function (replace the function call arguments)
    deed = generate_deed_of_partnership()

    # Create a PDF object and add content
    pdf = PDF()
    pdf.chapter_title(" ")
    pdf.chapter_body(deed)

    # Output the PDF to a file (you can save it to a different directory if needed)
    pdf_file_path = 'partnership_deed.pdf'
    pdf.output(pdf_file_path)

    # Return the PDF file as a response to the user
    return send_file(pdf_file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
