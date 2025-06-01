declare module 'framer-motion' {
  import { ComponentType } from 'react';

  export interface MotionProps {
    initial?: Record<string, number | string>;
    animate?: Record<string, number | string>;
    transition?: {
      delay?: number;
      duration?: number;
      ease?: string;
    };
    className?: string;
    children?: React.ReactNode;
    id?: string;
  }

  export interface Motion {
    div: ComponentType<MotionProps>;
    header: ComponentType<MotionProps>;
    section: ComponentType<MotionProps>;
    h1: ComponentType<MotionProps>;
    h2: ComponentType<MotionProps>;
    p: ComponentType<MotionProps>;
    span: ComponentType<MotionProps>;
    button: ComponentType<MotionProps>;
    form: ComponentType<MotionProps>;
    input: ComponentType<MotionProps>;
    label: ComponentType<MotionProps>;
  }

  export const motion: Motion;
} 