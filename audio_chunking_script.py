import sys

from pydub import AudioSegment


def slice_audio(input_file, chunk_size_ms, out_path, output_format='wav'):
    # Load the audio file
    audio = AudioSegment.from_file(input_file)

    # Calculate the total duration of the audio file in milliseconds
    total_duration = len(audio)

    # Calculate the number of chunks
    num_chunks = total_duration // chunk_size_ms

    for i in range(num_chunks):
        # Calculate the starting and ending positions for the current chunk
        start_time = i * chunk_size_ms
        end_time = start_time + chunk_size_ms

        # Extract the chunk
        chunk = audio[start_time:end_time]

        # Save the chunk to a new file
        output_file = f"{out_path}/chunk_{i + 1}.{output_format}"
        chunk.export(output_file, format=output_format)
        print(f"Chunk {i + 1} saved as '{output_file}'")


def main_method(input_file, chunk_size_ms, out_path):
    slice_audio(input_file, chunk_size_ms, out_path)


if __name__ == '__main__':
    input_file_path = sys.argv[0]
    frame_size = sys.argv[1]
    output_file_path = sys.argv[2]
    main_method(input_file_path, frame_size, output_file_path)

# TO RUN Kindly use below command 
# python3 .\audio_chunking.py input_file_path frame_size_in_milliseconds output_file_path
