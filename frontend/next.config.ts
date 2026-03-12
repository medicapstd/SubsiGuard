import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  async rewrites() {
    const isProd = process.env.NODE_ENV === 'production';
    return [
      {
        source: '/api/:path*',
        destination: isProd ? '/api/:path*' : 'http://127.0.0.1:8000/:path*',
      },
    ];
  },
};

export default nextConfig;
