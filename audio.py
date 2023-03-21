import pyaudio
import numpy as np

# Calculate frequency from pixel color
def freq_from_pixel(pixel):
    color_sum = pixel.red + pixel.green + pixel.blue
    note_index = round((color_sum / 765) * 39)
    return (2 ** ((note_index+69 - 81) / 12)) * 440

# Play sound for a given pixel
async def play_sound(pixel):
    duration = 0.5
    samples = (np.sin(2*np.pi*np.arange(sample_rate*duration)*freq_from_pixel(pixel)/sample_rate)).astype(np.float32)
    await asyncio.sleep(0)
    stream = p.open(format=audio_format, channels=num_channels, rate=sample_rate, output=True)
    stream.write(volume*samples)
    stream.close()
    await asyncio.sleep(0)
