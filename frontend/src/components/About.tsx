import { motion } from 'framer-motion';

export default function About() {
  return (
    <motion.section
      id="about"
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      className="py-16 bg-black/30 backdrop-blur-lg mt-16"
    >
      <div className="container mx-auto px-4">
        <motion.h2
          initial={{ y: -20 }}
          animate={{ y: 0 }}
          className="text-3xl font-bold text-white text-center mb-8"
        >
          Acerca del Proyecto
        </motion.h2>

        <div className="grid md:grid-cols-2 gap-8 max-w-4xl mx-auto">
          <motion.div
            initial={{ x: -20 }}
            animate={{ x: 0 }}
            className="bg-white/10 p-6 rounded-lg"
          >
            <h3 className="text-xl font-semibold text-white mb-4">
              ¿Cómo funciona?
            </h3>
            <p className="text-white/80">
              Nuestro clasificador utiliza modelos de inteligencia artificial
              entrenados con miles de muestras de vinos para predecir su calidad
              basándose en características químicas específicas.
            </p>
          </motion.div>

          <motion.div
            initial={{ x: 20 }}
            animate={{ x: 0 }}
            className="bg-white/10 p-6 rounded-lg"
          >
            <h3 className="text-xl font-semibold text-white mb-4">
              Características Analizadas
            </h3>
            <ul className="text-white/80 list-disc list-inside space-y-2">
              <li>Acidez fija y volátil</li>
              <li>Contenido de ácido cítrico</li>
              <li>Azúcares residuales</li>
              <li>Cloruros y sulfatos</li>
              <li>Dióxido de azufre</li>
              <li>Densidad y pH</li>
              <li>Contenido de alcohol</li>
            </ul>
          </motion.div>
        </div>

        <motion.div
          initial={{ y: 20 }}
          animate={{ y: 0 }}
          className="mt-12 text-center"
        >
          <p className="text-white/60 text-sm">
            Desarrollado por el equipo de IA - Universidad XYZ
          </p>
        </motion.div>
      </div>
    </motion.section>
  );
} 