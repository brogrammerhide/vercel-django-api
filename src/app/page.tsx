export default function Home() {
  return (
    <div className="min-h-screen bg-gray-50 flex flex-col justify-center items-center px-6 py-12">
      <main className="max-w-4xl w-full text-center">
        <h1 className="text-4xl sm:text-5xl font-extrabold text-gray-900 mb-4">
          Welcome to Your Next.js Tailwind Landing Page
        </h1>
        <p className="text-lg sm:text-xl text-gray-600 max-w-2xl mx-auto mb-8">
          Build beautiful, responsive interfaces with Tailwind CSS and Next.js quickly and easily.
          Mobile-first and optimized for all screen sizes.
        </p>
        <div className="flex flex-col sm:flex-row justify-center gap-4">
          <a
            href="#get-started"
            className="inline-block bg-blue-600 text-white px-8 py-3 rounded-md text-lg font-semibold hover:bg-blue-700 transition"
          >
            Get Started
          </a>
          <a
            href="#learn-more"
            className="inline-block border border-gray-300 px-8 py-3 rounded-md text-lg font-semibold text-gray-700 hover:bg-gray-100 transition"
          >
            Learn More
          </a>
        </div>
      </main>

      <footer className="mt-16 text-gray-500 text-sm">
        &copy; 2025 Your Company. All rights reserved.
      </footer>
    </div>
  );
}
