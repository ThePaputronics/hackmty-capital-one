import React from 'react';
import { interpolate, useCurrentFrame } from 'remotion';
import { theme } from '../theme';

export const Scene02Problem: React.FC = () => {
  const frame = useCurrentFrame();

  const titleOpacity = interpolate(frame, [0, 20], [0, 1], { extrapolateRight: 'clamp' });
  const stat1Opacity = interpolate(frame, [25, 45], [0, 1], { extrapolateRight: 'clamp' });
  const stat2Opacity = interpolate(frame, [60, 80], [0, 1], { extrapolateRight: 'clamp' });
  const alertOpacity = interpolate(frame, [110, 140], [0, 1], { extrapolateRight: 'clamp' });

  return (
    <div
      style={{
        flex: 1,
        backgroundColor: theme.colors.bg,
        display: 'flex',
        flexDirection: 'column',
        justifyContent: 'center',
        padding: '0 140px',
        position: 'relative',
      }}
    >
      <div style={{ opacity: titleOpacity, marginBottom: '60px' }}>
        <span
          style={{
            color: theme.colors.accent,
            fontFamily: theme.fonts.mono,
            fontSize: '16px',
            letterSpacing: '3px',
            textTransform: 'uppercase',
          }}
        >
          El Problema en México
        </span>
        <h1
          style={{
            color: theme.colors.textPrimary,
            fontFamily: theme.fonts.serif,
            fontSize: '56px',
            fontWeight: 600,
            marginTop: '10px',
            lineHeight: 1.15,
          }}
        >
          Liquidación instantánea e irreversible.
        </h1>
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '40px', marginBottom: '50px' }}>
        <div
          style={{
            opacity: stat1Opacity,
            backgroundColor: theme.colors.surface,
            border: `1px solid ${theme.colors.surfaceBorder}`,
            borderRadius: '16px',
            padding: '36px',
          }}
        >
          <div style={{ color: theme.colors.textMuted, fontSize: '15px', fontFamily: theme.fonts.mono, marginBottom: '12px' }}>
            BANXICO · AGOSTO 2026
          </div>
          <div style={{ color: theme.colors.textPrimary, fontSize: '54px', fontFamily: theme.fonts.mono, fontWeight: 700 }}>
            797.9M
          </div>
          <div style={{ color: theme.colors.textSecondary, fontSize: '18px', marginTop: '10px' }}>
            Operaciones SPEI en un solo mes ($29.93 billones de pesos)
          </div>
        </div>

        <div
          style={{
            opacity: stat2Opacity,
            backgroundColor: theme.colors.surface,
            border: `1px solid ${theme.colors.surfaceBorder}`,
            borderRadius: '16px',
            padding: '36px',
          }}
        >
          <div style={{ color: theme.colors.textMuted, fontSize: '15px', fontFamily: theme.fonts.mono, marginBottom: '12px' }}>
            CONDUSEF · ENE-MAY 2025
          </div>
          <div style={{ color: '#f87171', fontSize: '54px', fontFamily: theme.fonts.mono, fontWeight: 700 }}>
            35,762
          </div>
          <div style={{ color: theme.colors.textSecondary, fontSize: '18px', marginTop: '10px' }}>
            Reclamaciones por posible fraude con brecha en pagos autorizados manipulados (APP)
          </div>
        </div>
      </div>

      <div
        style={{
          opacity: alertOpacity,
          backgroundColor: 'rgba(239, 68, 68, 0.1)',
          borderLeft: '4px solid #ef4444',
          padding: '20px 28px',
          borderRadius: '4px',
        }}
      >
        <span style={{ color: '#fca5a5', fontSize: '20px', fontFamily: theme.fonts.serif }}>
          El usuario autenticado pasa el segundo factor porque está bajo coerción telefónica. <strong>Una vez liquidada la transferencia, no existe promesa de recuperación.</strong>
        </span>
      </div>
    </div>
  );
};
