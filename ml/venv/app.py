from flask import Flask, request, jsonify

app = Flask(__name__)

from compare import compare_pronunciations

@app.route('/compare', methods=['POST'])
def compare():
    if 'user_audio' not in request.files or 'ref_audio' not in request.files:
        return jsonify({'error': 'Missing audio files'}), 400

    user_audio = request.files['user_audio']
    ref_audio = request.files['ref_audio']

    # Save files temporarily
    user_audio_path = 'temp_user_audio.wav'
    ref_audio_path = 'temp_ref_audio.wav'
    user_audio.save(user_audio_path)
    ref_audio.save(ref_audio_path)

    # Perform comparison
    distance = compare_pronunciations(user_audio_path, ref_audio_path)

    # Here you can delete the temporary files if desired
    # os.remove(user_audio_path)
    # os.remove(ref_audio_path)

    return jsonify({"distance": distance})

if __name__ == "__main__":
    app.run(debug=True)
