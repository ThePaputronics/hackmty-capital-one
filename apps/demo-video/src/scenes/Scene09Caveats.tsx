import React from 'react';
import { interpolate, useCurrentFrame } from 'remotion';
import { theme } from '../theme';

export const Scene09Caveats: React.FC = () => {
  const frame = useCurrentFrame();

  const o1 = interpolate(frame, [0, 20], [0, 1], { extrapolateRight: 'clamp' });
  const o2 = interpolate(frame, [15, 35], [0, 1], { extrapolateRight: 'clamp' });

  return (
    <div
      style={{
        flex: 1,
        backgroundColor: theme.colors.bg,
        display: 'flex',
        flexDirection: 'column',
        justifyContent: 'center',
        padding: '0 140px',
      }}
    >
      <div style={{ marginBottom: '40px' }}>
        <span style={{ color: theme.colors.accent, fontFamily: theme.fonts.mono, fontSize: '15px', letterSpacing: '2px', textTransform: 'uppercase' }}>
          Transparencia y Supuestos
        </span>
        <h2 style={{ color: '#fff', fontFamily: theme.fonts.serif, fontSize: '46px', margin: '6px 0 0 0' }}>
          Honestidad sobre los Datos
        </h2>
      </div>

      <div style={{ display: 'flex', flexDirection: 'column', gap: '24px' }}>
        <div
          style={{
            opacity: o1,
            backgroundColor: theme.colors.surface,
            borderLeft: `4px solid ${theme.colors.accent}`,
            borderRadius: '4px',
            padding: '24px 30px',
          }}
        >
          <div style={{ color: '#fff', fontSize: '22px', fontFamily: theme.fonts.serif, fontWeight: 600, marginBottom: '6px' }}>
            Muestra Sintética Reproducible
          </div>
          <div style={{ color: theme.colors.textSecondary, fontSize: '16px', lineHeight: 1.5 }}>
            Los $146,800 pesos corresponden a exposición simulada dentro de la batería de pruebas controlada, no a dinero real rescatado.
          </div>
        </div>

        <div
          style={{
            opacity: o2,
            backgroundColor: theme.colors.surface,
            borderLeft: '4px solid #60a5fa',
            borderRadius: '4px',
            padding: '24px 30px',
          }}
        >
          <div style={{ color: '#fff', fontSize: '22px', fontFamily: theme.fonts.serif, fontWeight: 600, marginBottom: '6px' }}>
            Supuesto Declarado de Cancelación (p = 0.85)
          </div>
          <div style={{ color: theme.colors.textSecondary, fontSize: '16px', lineHeight: 1.5 }}>
            Asumimos una probabilidad del 85% de que un cliente cancela al ser confrontado con una advertencia específica contra engaños bancarios.
          </div>
        </div>
      </div>
    </div>
  );
};
