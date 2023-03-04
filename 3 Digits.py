import gradio as gr

def number_to_words(number):

    # Parse each digit
    digit_pertama = number // 100
    digit_kedua = (number // 10) % 10
    digit_ketiga = number % 10

    if digit_pertama == 1:
        word_form = "seratus "
    elif digit_pertama == 2:
        word_form = "dua ratus "
    elif digit_pertama == 3:
        word_form = "tiga ratus "
    elif digit_pertama == 4:
        word_form = "empat ratus "
    elif digit_pertama == 5:
        word_form = "lima ratus "
    elif digit_pertama == 6:
        word_form = "enam ratus "
    elif digit_pertama == 7:
        word_form = "tujuh ratus "
    elif digit_pertama == 8:
        word_form = "delapan ratus "
    elif digit_pertama == 9:
        word_form = "sembilan ratus "
    else:
        word_form = ""
    
    if digit_kedua == 1:
        if digit_ketiga == 0:
            word_form += "sepuluh"
        elif digit_ketiga == 1:
            word_form += "sebelas"
        elif digit_ketiga == 2:
            word_form += "dua belas"
        elif digit_ketiga == 3:
            word_form += "tiga belas"
        elif digit_ketiga == 4:
            word_form += "empat belas"
        elif digit_ketiga == 5:
            word_form += "lima belas"
        elif digit_ketiga == 6:
            word_form += "enam belas"
        elif digit_ketiga == 7:
            word_form += "tujuh belas"
        elif digit_ketiga == 8:
            word_form += "delapan belas"
        elif digit_ketiga == 9:
            word_form += "sembilan belas"
    else:
        if digit_kedua == 2:
            word_form += "dua puluh "
        elif digit_kedua == 3:
            word_form += "tiga puluh "
        elif digit_kedua == 4:
            word_form += "empat puluh "
        elif digit_kedua == 5:
            word_form += "lima puluh "
        elif digit_kedua == 6:
            word_form += "enam puluh "
        elif digit_kedua == 7:
            word_form += "tujuh puluh "
        elif digit_kedua == 8:
            word_form += "delapan puluh "
        elif digit_kedua == 9:
            word_form += "sembilan puluh "
        
        if digit_ketiga == 1:
            word_form += "satu"
        elif digit_ketiga == 2:
            word_form += "dua"
        elif digit_ketiga == 3:
            word_form += "tiga"
        elif digit_ketiga == 4:
            word_form += "empat"
        elif digit_ketiga == 5:
            word_form += "lima"
        elif digit_ketiga == 6:
            word_form += "enam"
        elif digit_ketiga == 7:
            word_form += "tujuh"
        elif digit_ketiga == 8:
            word_form += "delapan"
        elif digit_ketiga == 9:
            word_form += "sembilan"

    # return the word form of the number
    return word_form

inputs = gr.inputs.Number(label="Enter a 3-digit number")
outputs = gr.outputs.Textbox(label="Word form of the number")

gr.Interface(number_to_words, inputs, outputs, title="Number to Words Converter").launch()
