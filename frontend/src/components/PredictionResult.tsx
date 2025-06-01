import { motion } from 'framer-motion';

interface PredictionResultProps {
  prediction: number;
  category: string;
}

export default function PredictionResult({ prediction, category }: PredictionResultProps) {
  const getColorByCategory = () => {
    switch (category.toLowerCase()) {
      case 'bueno':
        return 'from-green-500 to-emerald-600';
      case 'regular':
        return 'from-yellow-500 to-orange-600';
      case 'malo':
        return 'from-red-500 to-red-700';
      default:
        return 'from-purple-500 to-indigo-600';
    }
  };

  return (
    <motion.div
      initial={{ opacity: 0, scale: 0.95 }}
      animate={{ opacity: 1, scale: 1 }}
      className={`mt-8 p-6 rounded-lg text-center bg-gradient-to-r ${getColorByCategory()} shadow-xl`}
    >
      <motion.h2 
        className="text-2xl font-bold text-white mb-4"
        initial={{ y: -20 }}
        animate={{ y: 0 }}
        transition={{ delay: 0.2 }}
      >
        Resultado del Análisis
      </motion.h2>
      
      <motion.div
        className="space-y-4"
        initial={{ y: 20 }}
        animate={{ y: 0 }}
        transition={{ delay: 0.3 }}
      >
        <div className="bg-white/20 rounded-lg p-4">
          <p className="text-sm text-white/80 mb-1">Puntuación</p>
          <p className="text-4xl font-bold text-white">{prediction.toFixed(1)}/10</p>
        </div>

        <div className="bg-white/20 rounded-lg p-4">
          <p className="text-sm text-white/80 mb-1">Categoría</p>
          <p className="text-2xl font-semibold text-white">{category}</p>
        </div>
      </motion.div>

      <motion.p
        className="mt-6 text-white/90 text-sm"
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.5 }}
      >
        Esta calificación está basada en las características químicas del vino
      </motion.p>
    </motion.div>
  );
} 