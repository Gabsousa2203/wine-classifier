"use client";

import { useState } from "react";
import { motion } from "framer-motion";
import toast from "react-hot-toast";
import Header from "@/components/Header";
import PredictionResult from "@/components/PredictionResult";
import About from "@/components/About";

interface WineFeatures {
  fixed_acidity: number;
  volatile_acidity: number;
  citric_acid: number;
  residual_sugar: number;
  chlorides: number;
  free_sulfur_dioxide: number;
  total_sulfur_dioxide: number;
  density: number;
  pH: number;
  sulphates: number;
  alcohol: number;
}

const initialFeatures: WineFeatures = {
  fixed_acidity: 7.4,
  volatile_acidity: 0.7,
  citric_acid: 0.0,
  residual_sugar: 1.9,
  chlorides: 0.076,
  free_sulfur_dioxide: 11,
  total_sulfur_dioxide: 34,
  density: 0.9978,
  pH: 3.51,
  sulphates: 0.56,
  alcohol: 9.4,
};

export default function Home() {
  const [features, setFeatures] = useState<WineFeatures>(initialFeatures);
  const [wineType, setWineType] = useState<"red" | "white">("red");
  const [loading, setLoading] = useState(false);
  const [prediction, setPrediction] = useState<{
    prediction: number;
    category: string;
  } | null>(null);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    try {
      const response = await fetch("http://localhost:8000/predict", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ ...features, wine_type: wineType }),
      });
      const data = await response.json();
      if (!response.ok) throw new Error(data.detail);
      setPrediction(data);
      toast.success("¡Predicción realizada con éxito!");
    } catch (error) {
      toast.error(error instanceof Error ? error.message : "Error al predecir");
    } finally {
      setLoading(false);
    }
  };

  return (
    <>
      <Header />
      <div className="container mx-auto px-4 py-8">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          className="max-w-2xl mx-auto bg-white/10 backdrop-blur-lg rounded-xl shadow-xl p-6"
        >
          <h1 className="text-4xl font-bold text-center mb-8 text-white">
            Análisis de Vino
          </h1>

          <form onSubmit={handleSubmit} className="space-y-6">
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              {Object.entries(features).map(([key, value]) => (
                <div key={key} className="form-control">
                  <label className="block text-sm font-medium text-white mb-1">
                    {key.split("_").join(" ").toUpperCase()}
                  </label>
                  <input
                    type="number"
                    step="any"
                    value={value}
                    onChange={(e) =>
                      setFeatures((prev) => ({
                        ...prev,
                        [key]: parseFloat(e.target.value),
                      }))
                    }
                    className="w-full px-3 py-2 bg-white/20 border border-gray-300 rounded-lg text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-purple-500"
                  />
                </div>
              ))}
            </div>

            <div className="flex justify-center space-x-4">
              <button
                type="button"
                onClick={() => setWineType("red")}
                className={`px-6 py-2 rounded-full ${
                  wineType === "red"
                    ? "bg-red-700 text-white"
                    : "bg-white/20 text-white"
                }`}
              >
                Vino Tinto
              </button>
              <button
                type="button"
                onClick={() => setWineType("white")}
                className={`px-6 py-2 rounded-full ${
                  wineType === "white"
                    ? "bg-amber-500 text-white"
                    : "bg-white/20 text-white"
                }`}
              >
                Vino Blanco
              </button>
            </div>

            <div className="flex justify-center">
              <button
                type="submit"
                disabled={loading}
                className="px-8 py-3 bg-gradient-to-r from-purple-600 to-pink-600 text-white rounded-full font-medium shadow-lg hover:from-purple-700 hover:to-pink-700 transition-all disabled:opacity-50"
              >
                {loading ? "Analizando..." : "Clasificar Vino"}
              </button>
            </div>
          </form>

          {prediction && (
            <PredictionResult
              prediction={prediction.prediction}
              category={prediction.category}
            />
          )}
        </motion.div>
      </div>
      <About />
    </>
  );
}
