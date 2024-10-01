const { exec } = require('child_process');
const path = require('path');
const videoPath = path.resolve('fromsempiller.mp4');

console.log("youre just got fanum taxed by agents")

const fs = require('fs');
if (fs.existsSync(videoPath)) {
    let command;

    switch (process.platform) {
        case 'win32':
            command = `start "" "${videoPath}"`;
            break;
        case 'darwin':
            command = `open "${videoPath}"`;
            break;
        case 'linux':
            command = `xdg-open "${videoPath}"`;
            break;
        default:
            process.exit(1);
    }

    exec(command, (error) => {
        if (error) {
            return;
        }
    });
}