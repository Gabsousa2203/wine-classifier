import { motion } from 'framer-motion';

export default function Header() {
  return (
    <motion.header
      initial={{ opacity: 0, y: -20 }}
      animate={{ opacity: 1, y: 0 }}
      className="py-6 mb-8"
    >
      <div className="container mx-auto px-4">
        <div className="flex items-center justify-between">
          <motion.h1 
            className="text-3xl font-bold text-white"
            initial={{ opacity: 0, x: -20 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ delay: 0.2 }}
          >
            🍷 Wine Classifier
          </motion.h1>
          <motion.div
            className="flex space-x-4"
            initial={{ opacity: 0, x: 20 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ delay: 0.3 }}
          >
            <a
              href="https://github.com/Gabsousa2203/wine-classifier/tree/main"
              target="_blank"
              rel="noopener noreferrer"
              className="text-white hover:text-purple-300 transition-colors"
            >
              GitHub
            </a>
            <a
              href="#about"
              className="text-white hover:text-purple-300 transition-colors"
            >
              Acerca de
            </a>
          </motion.div>
        </div>
      </div>
    </motion.header>
  );
} 