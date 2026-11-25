# Record your Gaussian elimination voice-over

Use the timestamp ranges in **Narration_Script.md** with the silent **_Video.mp4**. You only need to record your voice. The video already contains the visuals and timing.

1. **Set up.** Use a quiet room and headphones. Position the microphone about a hand’s width from your mouth. Record a short test and play it back to check that your words are clear.
2. **Add the video to your editor.** Put the MP4 at 00:00. Keep its full 5:00 length. Open the script beside the editor.
3. **Record in sections.** Set the playhead to the start of a timestamped section, read its paragraph aloud, and stop. Repeat at each cue. If you’re recording on your phone, record one clip per section and place each clip at its time in the editor. If you finish a section early, let the visuals play until the next cue.
4. **Match your words to the motion.** The first row update starts at 01:54, the next at 02:07, and the last at 02:27. Let the cells change as you explain the subtraction. In the back-substitution section, watch for the z, y, and x reveals at 02:51, 03:00, and 03:12.
5. **Export and verify.** Export an MP4 at 1920 × 1080. Play it back to check that your voice is audible throughout, the name and ID are visible at the start, and the recap and credits are visible at the end. Use the narrated export as the repository’s `_Video.mp4`.

If you already have one edited voice recording that starts at 00:00, you can also combine it with the video using FFmpeg. Run this from the project directory, replacing `voiceover.m4a` with your own filename.

```sh
ffmpeg -i _Video.mp4 -i voiceover.m4a -map 0:v:0 -map 1:a:0 \
  -c:v copy -c:a aac -b:a 192k -af apad -t 300 -movflags +faststart Narrated_Video.mp4
```

Review `Narrated_Video.mp4` before renaming it to `_Video.mp4` for submission. The public repository should also include the storyboard, script, and complete source code. Submit its URL using the official Google Form.
