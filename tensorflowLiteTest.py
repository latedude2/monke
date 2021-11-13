import tflite_runtime.interpreter as tflite
interpreter = tflite.Interpreter('model.tflite')
interpreter.allocate_tensors()
interpreter.get_input_details()
output_details = interpreter.get_output_details()
print(output_details)