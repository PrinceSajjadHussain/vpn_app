document.addEventListener('DOMContentLoaded', (event) => {
    const vpnToggle = document.getElementById('vpn-toggle');
    const statusText = document.getElementById('status');
    const connectionStatus = document.getElementById('connection-status');

    vpnToggle.addEventListener('change', () => {
        if (vpnToggle.checked) {
            statusText.textContent = 'VPN is on';
            // Here you can add the logic to connect to the VPN
            connectVPN();
        } else {
            statusText.textContent = 'VPN is off';
            // Here you can add the logic to disconnect from the VPN
            disconnectVPN();
        }
    });

    function connectVPN() {
        // Replace with actual VPN connection logic
        connectionStatus.textContent = 'Connecting...';
        setTimeout(() => {
            connectionStatus.textContent = 'Connected';
            connectionStatus.classList.add('connected');
        }, 2000); // Simulate connection delay
    }

    function disconnectVPN() {
        // Replace with actual VPN disconnection logic
        connectionStatus.textContent = 'Disconnecting...';
        setTimeout(() => {
            connectionStatus.textContent = 'Not connected';
            connectionStatus.classList.remove('connected');
        }, 2000); // Simulate disconnection delay
    }
});
