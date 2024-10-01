const net = require('net');
const dgram = require('dgram');
const process = require('process');

const [,, protocol, ip, port, message] = process.argv;

const printAttackDetails = () => {
    console.clear();
    const width = process.stdout.columns || 80; 
    console.log(' '.repeat((width - 30) / 2) + "EagleWare Fun Mode");
    console.log(' '.repeat((width - 40) / 2) + "╔════════════════════════════════╗");
    console.log(' '.repeat((width - 40) / 2) + ` Target IP: ${ip}`);
    console.log(' '.repeat((width - 40) / 2) + ` Port: ${port}`);
    console.log(' '.repeat((width - 40) / 2) + ` Message: ${message}`);
    console.log(' '.repeat((width - 40) / 2) + ` Method: ${protocol.toUpperCase()}`);
    console.log(' '.repeat((width - 40) / 2) + "╚════════════════════════════════╝");
};

if (protocol === 'tcp') {
    const client = new net.Socket();

    client.connect(port, ip, () => {
        printAttackDetails();
        client.write(message);
    });

    client.on('data', (data) => {
        console.log('Reply: ' + data);
        client.destroy();
    });

    client.on('error', (err) => {
        console.error('Error:', err);
    });

    client.on('close', () => {
        console.log('IP Closed');
    });

} else if (protocol === 'udp') {
    const client = dgram.createSocket('udp4');
    const msgBuffer = Buffer.from(message);

    client.send(msgBuffer, port, ip, (err) => {
        if (err) {
            console.error('Error while sending:', err);
        } else {
            printAttackDetails();
            console.log('Message sent');
        }
        client.close();
    });

    client.on('message', (msg) => {
        console.log('Reply: ' + msg.toString());
    });

    client.on('error', (err) => {
        console.error('Error:', err);
    });
}
