import React from 'react';
import { interpolate, useCurrentFrame } from 'remotion';
import { theme } from '../theme';

export const Scene10Outro: React.FC = () => {
  const frame = useCurrentFrame();

  const o1 = interpolate(frame, [0, 20], [0, 1], { extrapolateRight: 'clamp' });
  const o2 = interpolate(frame, [25, 45], [0, 1], { extrapolateRight: 'clamp' });

  return (
    <div
      style={{
        flex: 1,
        backgroundColor: theme.colors.bg,
        display: 'flex',
        flexDirection: 'column',
        justifyContent: 'center',
        alignItems: 'center',
        textAlign: 'center',
        padding: '0 100px',
      }}
    >
      <div style={{ opacity: o1, marginBottom: '24px' }}>
        <h1
          style={{
            color: '#fff',
            fontFamily: theme.fonts.serif,
            fontSize: '52px',
            maxWidth: '900px',
            lineHeight: 1.25,
            margin: '0 auto',
          }}
        >
          "Intervenir antes del envío, porque después ya no hay promesa posible."
        </h1>
      </div>

      <div style={{ opacity: o2, marginTop: '20px' }}>
        <div
          style={{
            display: 'inline-block',
            backgroundColor: 'rgba(216, 155, 66, 0.15)',
            border: `1.5px solid ${theme.colors.accent}`,
            borderRadius: '12px',
            padding: '16px 36px',
            color: theme.colors.accentLight,
            fontFamily: theme.fonts.mono,
            fontSize: '26px',
            fontWeight: 700,
            letterSpacing: '1px',
            marginBottom: '20px',
          }}
        >
          sixsevencitos.tech
        </div>
        <div style={{ color: theme.colors.textMuted, fontSize: '16px', fontFamily: theme.fonts.mono }}>
          API Docs: sixsevencitos.tech/docs · Reto Capital One · HackMTY 2026
        </div>
      </div>
    </div>
  );
};
