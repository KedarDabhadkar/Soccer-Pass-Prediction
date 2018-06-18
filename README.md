# Soccer-Pass-Prediction
Development of a model which predicts which player the ball is passed to in a soccer match when the location of all 22 players on the field is given.

The dataset can be obtained from https://github.com/JanVanHaaren/mlsa18-pass-prediction.

README.md of the parent file says:

## Dataset

The dataset contains 12,124 passes performed during 14 different games involving a Belgian football club during the 2014/2015 football season.

### Format

The `passes.csv` file contains the dataset in a comma-separated format. The file contains 12,125 rows and 60 columns. In addition to a header row, the file contains one row for each pass providing the following information:
- `time_start`: time elapsed in milliseconds since the start of the half at the time the ball was passed by the sender;
- `time_end`: time elapsed in milliseconds since the start of the half at the time the ball was received by the receiver;
- `sender_id`: the identifier of the player who passed the ball;
- `receiver_id`: the identifier of the player who received the ball;
- `x_*`: the x coordinates of the locations of the players on the pitch at the time of the pass;
- `y_*`: the y coordinates of the locations of the players on the pitch at the time of the pass.

### Identifiers

The players within each game are numbered from 1 till 28. Each team consists of 14 players: 11 starters and 3 substitutes. The players numbered from 1 till 14 belong to the home team, whereas the players numbered from 15 to 28 belong to the away team. Since the data were collected during different games involving different teams, the identifiers are only relevant within the scope of a single pass.

### Coordinates

The coordinates are expressed in centimeters in both directions of the pitch. The pitch is 105 meters long and 68 meters wide. The x-axis represents the long side of the pitch, whereas the y-axis represents the short side of the pitch:
- `(0, 0)`: center of the pitch;
- `(-5250, -3400)`: top-left corner of the pitch;
- `(-5250, 3400)`: bottom-left corner of the pitch;
- `(5250, -3400)`: top-right corner of the pitch;
- `(5250, 3400)`: bottom-right corner of the pitch.

## Contact

If you have any questions, suggestions or remarks, then please get in touch with Jan Van Haaren (j.vanhaaren@scisports.com). If you plan to participate in the challenge and submit a paper to the workshop, then please inform Jan Van Haaren as well. He will get in touch whenever any important information regarding the challenge would become available.
