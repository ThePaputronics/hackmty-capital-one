import React from 'react';
import { interpolate, useCurrentFrame } from 'remotion';
import { theme } from '../theme';

export const Scene03Question: React.FC = () => {
  const frame = useCurrentFrame();

  const card1Opacity = interpolate(frame, [0, 20], [0, 1], { extrapolateRight: 'clamp' });
  const card2Opacity = interpolate(frame, [35, 55], [0, 1], { extrapolateRight: 'clamp' });
  const card2Scale = interpolate(frame, [35, 55], [0.95, 1], { extrapolateRight: 'clamp' });

  return (
    <div
      style={{
        flex: 1,
        backgroundColor: theme.colors.bg,
        display: 'flex',
        flexDirection: 'column',
        justifyContent: 'center',
        alignItems: 'center',
        padding: '0 100px',
      }}
    >
      <div style={{ textAlign: 'center', marginBottom: '50px' }}>
        <span
          style={{
            color: theme.colors.accent,
            fontFamily: theme.fonts.mono,
            fontSize: '15px',
            letterSpacing: '3px',
            textTransform: 'uppercase',
          }}
        >
          El Cambio de Paradigma
        </span>
      </div>

      <div style={{ display: 'flex', gap: '50px', width: '100%', maxWidth: '1280px' }}>
        {/* Antiguo paradigma */}
        <div
          style={{
            flex: 1,
            opacity: card1Opacity,
            backgroundColor: theme.colors.surface,
            border: `1px solid ${theme.colors.surfaceBorder}`,
            borderRadius: '20px',
            padding: '50px 40px',
            display: 'flex',
            flexDirection: 'column',
          }}
        >
          <div style={{ color: '#ef4444', fontSize: '18px', fontWeight: 700, fontFamily: theme.fonts.mono, marginBottom: '20px' }}>
            ✕ ENFOQUE TRADICIONAL
          </div>
          <div style={{ color: '#8e94a5', fontSize: '38px', fontFamily: theme.fonts.serif, lineHeight: 1.25, marginBottom: '20px' }}>
            "¿Es realmente el cliente?"
          </div>
          <div style={{ color: theme.colors.textMuted, fontSize: '18px', lineHeight: 1.5 }}>
            Verifica credenciales, biometría y dispositivo. Falla completamente si el dueño legítimo de la cuenta es quien teclea bajo engaño.
          </div>
        </div>

        {/* Paradigma F.R.E.D */}
        <div
          style={{
            flex: 1,
            opacity: card2Opacity,
            transform: `scale(${card2Scale})`,
            backgroundColor: '#1b2233',
            border: `2px solid ${theme.colors.accent}`,
            borderRadius: '20px',
            padding: '50px 40px',
            display: 'flex',
            flexDirection: 'column',
            boxShadow: '0 0 50px rgba(216, 155, 66, 0.25)',
          }}
        >
          <div style={{ color: theme.colors.accentLight, fontSize: '18px', fontWeight: 700, fontFamily: theme.fonts.mono, marginBottom: '20px' }}>
            ✓ ENFOQUE F.R.E.D (SENTINEL)
          </div>
          <div style={{ color: '#ffffff', fontSize: '38px', fontFamily: theme.fonts.serif, lineHeight: 1.25, marginBottom: '20px' }}>
            "¿El cliente autenticado está siendo manipulado?"
          </div>
          <div style={{ color: '#c7cddf', fontSize: '18px', lineHeight: 1.5 }}>
            Evalúa la anomalía conductual de la intención y la red receptora sin juzgar sólo la identidad.
          </div>
        </div>
      </div>
    </div>
  );
};
