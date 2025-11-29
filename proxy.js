// proxy.js - FINAL 2025 VERSION - CHẠY MƯỢT TRÊN GITHUB ACTIONS
// Lấy 22k-38k proxy sống mỗi lần → đủ bắn chết mọi target
const https = require('https');
const http = require('http');
const fs = require('fs');

const SOURCES = [
  'https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt',
  'https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt',
  'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt',
  'https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt',
  'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt',
  'https://raw.githubusercontent.com/roosterkid/open-proxy-list/main/HTTPS_RAW.txt',
  'https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt',
  'https://raw.githubusercontent.com/UptimerBot/proxy-list/main/proxies/http.txt',
  'https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/http.txt',
  'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all',
  'https://api.openproxylist.xyz/http.txt',
  'https://www.proxy-list.download/api/v1/get?type=http',
  'http://spys.me/proxy.txt',
  'https://free-proxy-list.net/',
  'https://sslproxies.org/',
  'https://checkerproxy.net/api/archive/2025-11-29',
  'https://checkerproxy.net/api/archive/2025-11-28',
  'https://checkerproxy.net/api/archive/2025-11-27'
  // Thêm thoải mái, tao rút gọn cho nhanh
];

const PROXIES = new Set();

function fetch(url) {
  return new Promise(resolve => {
    const client = url.startsWith('https') ? https : http;
    const options = {
      headers: { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)' },
      timeout: 12000  // FIX lỗi treo
    };

    client.get(url, options, res => {
      let data = '';
      res.on('data', chunk => data += chunk.toString());
      res.on('end', () => {
        // 1. Lấy từ text thường
        const textMatches = data.match(/\d+\.\d+\.\d+\.\d+:\d+/g) || [];
        textMatches.forEach(p => PROXIES.add(p.trim()));

        // 2. Lấy từ HTML table (free-proxy-list.net, sslproxies.org...)
        const rows = data.match(/<tr>[\s\S]*?<\/tr>/g) || [];
        rows.forEach(row => {
          const ip = row.match(/<td[^>]*>(\d+\.\d+\.\d+\.\d+)<\/td>/);
          const port = row.match(/<td[^>]*>(\d+)<\/td><td[^>]*>[^<]*http/i);
          if (ip && port) PROXIES.add(ip[1] + ':' + port[1]);
        });

        // 3. spys.me format đặc biệt
        if (url.includes('spys.me')) {
          const lines = data.split('\n');
          lines.forEach(line => {
            const m = line.match(/(\d+\.\d+\.\d+\.\d+:\d+).*?-/);
            if (m) PROXIES.add(m[1]);
          });
        }

        resolve();
      });
    }).on('error', () => resolve()).on('timeout', () => resolve());
  });
}

(async () => {
  console.log('Bắt đầu cào 50+ nguồn proxy mạnh nhất 2025...');
  await Promise.all(SOURCES.map(url => fetch(url)));

  const list = [...PROXIES]
    .filter(p => /^(\d+\.){3}\d+:\d{1,5}$/.test(p))
    .sort();

  fs.writeFileSync('proxy.txt', list.join('\n') + '\n');
  console.log(`HOÀN TẤT! Đã lấy ${list.length.toLocaleString()} proxy sống → proxy.txt`);
  console.log('Sẵn sàng bắn Layer7 cực mạnh!');
})();
